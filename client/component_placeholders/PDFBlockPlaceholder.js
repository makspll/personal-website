import React from 'react';
import PDFObject from 'pdfobject';
import {UncontrolledCollapse} from 'reactstrap'
import Skeleton from 'react-loading-skeleton';
import Spinner from './Spinner';
class PDFBlockPlaceholder extends React.Component{

    render(){
        let idx = this.props.index;

        return(
            <div className="flex-grow-1 d-flex flex-column card">
                <button id={`collapse-${idx}`} className="rounded-0 text-reset text-decoration-none btn btn-link card-header collapse-arrow-container"  >
                    <h2><Skeleton width={150}/></h2>
                    <p className="card-text"><Skeleton width={100}/></p>
                    <i className="fa fa-angle-down fa-2x collapse-arrow inverted"></i>
                </button>
                <UncontrolledCollapse toggler={`collapse-${idx}`} defaultOpen={true}>
                    <div className="card-body p-0">
                        <div id="document-holder" className=" vh-100 d-flex flex-column justify-content-center">
                            <Spinner/>
                        </div>
                    </div>
                    <div className="card-footer">
                        <p className="text-muted mb-0" ><Skeleton/></p>
                    </div>
                </UncontrolledCollapse>
            </div>
        )
    }
}

export default PDFBlockPlaceholder;
