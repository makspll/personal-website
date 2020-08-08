import React from 'react';
import {GET_ROOT_URL,GET_API_ROOT_URL} from '../DynamicVariables.js';
import ContentLoader from "react-content-loader";
import ProjectListingBlock from "./ProjectListingBlock.js";


class FreeformListingBlock extends React.Component{

    constructor(props){
        super(props);
        this.state = {
            isLoaded: false,
            freeform_content: null,
        }
    }

    componentDidMount() {
        // find which page we're attached to 
        var url_href = GET_API_ROOT_URL() + `pages/find/?html_path=${window.location.pathname}`;

        fetch(url_href).then(res => res.json())
            .then( 
                (result) =>{
                    this.setState({
                        isLoaded: true,
                        freeform_content: result.freeform_items,
                    });
                },
                (error)=>{
                    console.error(error);
                }
            )
    }

    render() { 
        const  {isLoaded, freeform_content} = this.state;

        let content = null;

        if(isLoaded){
            // map each json block value to the corresponding react components
            let blocks = freeform_content.map((value,index)=>{

                let jsx_value = null;

                switch(String(value.type)){

                    case "text":
                        jsx_value = 
                            <div key={index} className="px-4">
                                text
                            </div>
                        break;
                    
                    case "projects":
                        jsx_value = 
                            <ProjectListingBlock key={index} json={value} isLoaded={true}/>
                        break;

                    default:
                        jsx_value =
                            <p key={index} >block type not implemented yet: {value.type} </p>
                        break;
                }
                
                return (
                        jsx_value
                        //                        {(index !== freeform_content.length - 1) ? <hr /> : null}

                )
            })

            content = blocks
                
        } else {

            let numrows = 10;

            var rows = [];

            for (var i = 0; i < numrows; i++) {
                rows.push(
                    <ProjectListingBlock key={i}/>
                );
            }

            content = rows;

        }
        
        return ( content )
    }

}

export default FreeformListingBlock;