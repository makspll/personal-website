import React from 'react';
import {GET_ROOT_URL,GET_API_ROOT_URL} from '../DynamicVariables.js';
import ContentLoader from "react-content-loader"

class TagFilterNav extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            tag_list: [],
            is_loaded : false,
        }
    }

    load_tags_page(){
        var url_href = GET_API_ROOT_URL() + `tags/`;

        fetch(url_href).then(res => res.json())
            .then( 
                (result) =>{
                    let aggregated_tag_names = result.flatMap((val)=>
                        val.name
                    )
                    this.setState({
                        tag_list : aggregated_tag_names,
                        is_loaded : true,
                    });
                },
                (error)=>{
                    console.error(error);
                }
            )
    }

    componentDidMount() {
        this.load_tags_page()
    }

    render() { 

        let {is_loaded, tag_list} = this.state;
        
        let content = null;
        if(is_loaded){

            let tags = tag_list.map((val,index)=>
                <span className="badge badge-secondary m-1">{val}</span>
            )

            content = 
                <nav className="bg-primary text-light border border-gray p-2 overflow-auto">
                    <h3 className="m-0 text-left">Filters</h3>
                    <hr className="my-2 bg-light"/>
                    <div className="d-flex flex-row flex-wrap">
                        {tags}
                    </div>
                </nav>
        }else{
            content = null;
        }
        return(content);    
}

}

export default TagFilterNav
