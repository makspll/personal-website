import React from 'react';
import {GET_API_ROOT_URL} from '../DynamicVariables.js';
import ArticleListing from './ArticleListing';

class ArticleListingBlock extends React.Component{
    
    constructor(props){
        super(props);
        this.state = {
            is_loaded : false,
            articles_json : null,
            page_no : 0,
        }
    }

    componentDidMount(){
        // find out which page we're on
        let url_href = `${GET_API_ROOT_URL()}pages/find/?html_path=${window.location.pathname}`;
        fetch(url_href)
            .then((res)=> {
                if(res.ok){
                    return res.json()
                }else{
                    throw `Couldn't fetch articles, status code: ${res.status}`
                }
            })
            .then(
                (response)=>{
                    this.setState({
                        is_loaded: true,
                        articles_json: response,
                    })
                },
                (error) =>{
                    this.setState({
                        is_loaded: true,
                    })
                    console.error(error);
                }
            )
    }

    set_page_no(page_number){
        this.setState({
            page_no:page_number,
        })
    }

    calculate_articles_max_no(){
        return (this.state.page_no+1) * (3 + Math.pow(this.state.page_no,2));
    }

    render(){
        let {is_loaded,articles_json} = this.state;
        
        let content = null;
        let show_more_btn = null;

        let data_present = is_loaded && articles_json;


        if(data_present){

            // increase amount of articles per click on "show more" by consant * exponential
            let articles_max_no = this.calculate_articles_max_no();

            let visible_articles_no = Math.min(articles_max_no,articles_json.articles.length)

            let visible_articles = articles_json.articles.slice(0,visible_articles_no);

            let article_listings = visible_articles.map((value,index)=>
                    <ArticleListing key={index} json={value} is_loaded={true} article_index={index} article_count={visible_articles_no}/>
            ) 

            content = article_listings;
            show_more_btn = (articles_max_no < articles_json.articles.length) ?
                <button className="btn btn-primary btn-large" onClick={()=>this.set_page_no(this.state.page_no + 1)}>Show More</button>:
                null

        } else if(is_loaded){
            content = <p>Oops! Looks like we could not retrieve data to display! Please refresh the page.</p>
        } else {
            content = null;
        }


        return (
            <React.Fragment>
                <div className="article-listing-body px-5 pt-5">
                    {content}
                </div>
                <div className="text-center p-3">
                {show_more_btn}
                </div>
            </React.Fragment>
        );
                
    }
}

export default ArticleListingBlock;