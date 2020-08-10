import React from 'react';
import {GET_ROOT_URL,GET_API_ROOT_URL} from '../DynamicVariables.js';
import ContentLoader from "react-content-loader";
import ProjectListingBlock from "./ProjectListingBlock.js";
import RichTextBlock from "./RichTextBlock.js";
import TimelineBlock from "./TimelineBlock.js";
import PDFBlock from "./PDFBlock.js";
import CodeBlock from "./CodeBlock.js";
import { data } from 'jquery';
import Spinner from '../component_placeholders/Spinner';
import FadeIn from 'react-fade-in';

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

        fetch(url_href)
            .then(res => {
                if(res.ok){
                    return res.json()
                }else{
                    throw `Couldn't fetch content, status code: ${res.status}`
                }
            })
            .then( 
                (result) =>{

                    this.setState({
                        isLoaded: true,
                        freeform_content: result.freeform_items,
                    });    
                       
                    
                   },
                (error)=>{
                    this.setState({
                        isLoaded: true,
                    })
                    console.error(error);
                }
            )
    }

    render() { 
        const  {isLoaded, freeform_content} = this.state;

        let content = null;

        let data_present = isLoaded && freeform_content;
        if(data_present){
            // map each json block value to the corresponding react components
            let blocks = freeform_content.map((value,index)=>{

                let jsx_value = null;

                switch(value.type){

                    case "text":
                        jsx_value = 
                            <div className="px-4">
                                <RichTextBlock key={index} json={value} isLoaded={true} idx={index} />
                            </div>
                        break;
                    case "timeline":
                        jsx_value = 
                            <TimelineBlock key={index} json={value} isLoaded={true} idx={index}/>
                        break;
                    case "projects":
                        jsx_value = 
                            <ProjectListingBlock key={index} json={value} isLoaded={true} idx={index}/>
                        break;
                    case "pdf":
                        jsx_value = 
                            <PDFBlock key={index} json={value} isLoaded={true} idx={index}/>
                        break;
                    case "code":
                        jsx_value =
                            <CodeBlock key={index} json={value} isLoaded={true} idx={index}/>
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

        } else if(isLoaded) {
            // on loaded but failed response
            content = <p>Oops! Looks like we could not retrieve data to display! Please refresh the page.</p>
        } else {

            content = 
                    <FadeIn 
                        delay={250} 
                        className="d-flex flex-column flex-grow-1"
                        childClassName="d-flex flex-column flex-grow-1">
                        <Spinner/>
                    </FadeIn>;

        }
        
        return ( content )
    }

}

export default FreeformListingBlock;
