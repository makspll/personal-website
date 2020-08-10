import React from 'react';
import Skeleton from 'react-loading-skeleton';
import {shuffle} from '../js/utils';

const ProjectBlockPlaceholder = (props) =>{
    let widths = ["calc(100% - 150px) ","calc(100% - 100px) ","calc(100% - 50px) "]
    widths = shuffle(widths);

    return (
        <li className="project-listing-project p-3 border position-relative">
            <div className="text-center text-sm-left mx-auto overflow-hidden">
            <Skeleton width={250} height={250} className="mr-sm-3 "/>
            </div>
            <div className="project-listing-project-body">
                <h4 className="h2 mb-0"><Skeleton /></h4>
                <div className="text-muted h6 mb-5">
                <span>
                    <i className="fa fa-hourglass-start fa-sm" aria-hidden="true"></i></span>
                    <span> <Skeleton width={100}/> -
                    </span>
                    <span> <i className="fa fa-hourglass-end fa-sm" aria-hidden="true"></i></span>
                    <span> <Skeleton width={100}/></span>
                    <br/>
                </div>
                    {widths.map((value,index)=>{
                        return <p><Skeleton width={value}/></p>
                        
                    })}
            </div>
        </li>
       
    );
}

export default ProjectBlockPlaceholder