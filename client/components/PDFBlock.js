import React from 'react';
import { GET_ROOT_URL,GET_API_ROOT_URL } from '../DynamicVariables.js';
import $ from "jquery";
import PDFObject from 'pdfobject';
import {UncontrolledCollapse} from 'reactstrap'

class PDFBlock extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            document_loaded:false,
            document_json:null,
            collapsed:false,
        }
    }

    componentDidMount(){
        let value = this.props.json.value;
        fetch(`${GET_API_ROOT_URL()}documents/${value.document}`)
            .then(
                (res) => {
                    if(res.ok){
                        return res.json();
                    } else{
                        throw  `Couldn't fetch articles, status code: ${res.status}`
                    }
                }
            )
            .then(
                (response)=>{
                    this.setState({
                            document_loaded: true,
                            document_json:response,
                        })
                },
                (error)=>{
                    this.setState({
                        document_loaded: true,
                    })
                    console.error(error);
                }
            )       

    }

    componentDidUpdate(){
        if(this.state.document_loaded){
            PDFObject.embed(`${GET_ROOT_URL()}document/view/${this.state.document_json.id}/${this.state.document_json.title}`,"#document-holder");
            $('.bootstrap-toggle').collapse()   
     
        }
    }

    render(){

        let {isLoaded,json} = this.props;

        let content = null;
        if (isLoaded && this.state.document_loaded){

            let {title,description,document} = json.value;
            let {idx} = this.props;
            content =
                <div className="flex-grow-1 d-flex flex-column card">
                    <button id={`collapse-${idx}`} className="rounded-0 text-reset text-decoration-none btn btn-link card-header collapse-arrow-container"  >
                        <h2>{title}</h2>
                        <p className="card-text">{description}</p>
                        <i className="fa fa-angle-down fa-2x collapse-arrow inverted"></i>
                    </button>
                    <UncontrolledCollapse toggler={`collapse-${idx}`} defaultOpen={true}>
                        <div className="card-body p-0">
                            <div id="document-holder" className=" vh-100 d-flex flex-column justify-content-center">
                                <p className="p-5">Your browser doesn't support embedded PDF's, help yourself with a download below:</p>
                                <a className="btn btn-primary align-self-center mb-5" href={ document.url}>Download PDF</a>
                            </div>
                        </div>
                        <div className="card-footer">
                            <p className="text-muted mb-0" >should the embedded document fail to show and the fallback not trigger <a href={document.url}>click here</a></p>
                        </div>
                    </UncontrolledCollapse>
                    <style dangerouslySetInnerHTML={{__html:
                        `.pdfobject {
                            display:flex;
                            flex-grow:1;
                        }`
                    }}>
                        
                    </style>
                </div>

        }else {
            content = null;
        }
        return content;
    }
}

export default PDFBlock;
