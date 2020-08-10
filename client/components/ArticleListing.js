import React from 'react';
import truncate from 'truncate-html';
import { LazyLoadImage } from 'react-lazy-load-image-component';
import ArticleListingPlaceholder from '../component_placeholders/ArticleListingPlaceholder';

import {GET_API_ROOT_URL} from '../DynamicVariables';
class ArticleListing extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            article_loaded: false,
            article_json: null,
        }
    }

    load_project_detail(){
        let {json} = this.props;
        fetch(`${GET_API_ROOT_URL()}pages/${json.id}`)
            .then((res)=>{
                if(res.ok){
                    return res.json();
                }else{
                    throw `Couldn't fetch articles, status code: ${res.status}`
                }
            })
            .then((res)=>{
                this.setState({
                    article_loaded:true,
                    article_json:res,
                })
            },
            (err)=>{
                console.error(err);
            })

    }

    componentDidMount(){
        if(this.props.is_loaded){
            this.load_project_detail()
        }
    }
    componentDidUpdate(prevProps,prevState,snapshot){
        if(!prevProps.is_loaded && this.props.is_loaded){
            this.load_project_detail()
        } 
    }

    render(){
        let {article_loaded,article_json} = this.state;
        let {is_loaded,json,article_index,article_count} = this.props;

        let content = null;
        let initial_data_present = is_loaded && json;

        if(initial_data_present && article_loaded && article_json){
            let tags = article_json.tags.map((value,index)=>
                <span className="badge badge-secondary mt-2 mr-2"> { value } </span>
            )


            let image = null;
            if(article_json.featured_image){
                let image_title = article_json.featured_image.title;
                let image_json = article_json.featured_image_original;
                let placeholder_img_json = article_json.featured_image_placeholder;
    
                image = 
                    <LazyLoadImage
                        alt={image_title}
                        src={image_json.url}
                        height={image_json.height}
                        width={image_json.width}
                        className="img-fluid article-listing-thumbnail img-thumbnail"
                        effect="blur"
                        placeholderSrc={placeholder_img_json.url}
                        wrapperProps={{style:{}}}
                    />
            }
           
            let date = new Date(article_json.meta.first_published_at)

            content = 
                <div className="article-listing-article pt-5 position-relative text-left pt-3" >
                    <h2 className="mb-0">{article_json.title}</h2>
                    <div >
                        <div className="text-muted h6">

                            <span><i className="far fa-clock fa-sm" aria-hidden="true"></i></span>
                            <span> {`${date.toLocaleDateString()}`}</span>
                            <br/>
                            {tags}
                        </div>
                    </div>
                    {image}
                    <a href={article_json.meta.html_url} className="stretched-link"></a>
                    <p dangerouslySetInnerHTML={{__html:truncate(article_json.blurb,600)}}></p>
                    <div className="overlay">Read More</div>
                    <hr className="mb-0"/>
 
                </div>
        } else if (article_loaded && !article_json) {
            return <p>Could not load data, please refresh the page.</p>
        } else {
            return <ArticleListingPlaceholder/>
        }  

        return content;
    }
}

export default ArticleListing;