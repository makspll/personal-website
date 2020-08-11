import React from 'react';
import {GET_API_ROOT_URL} from '../DynamicVariables';
import Skeleton, { SkeletonTheme } from 'react-loading-skeleton';

class LinkCardBlockPlaceholder extends React.Component{

    render(){
        let {index} = this.props;

        let color_variables = ["blue","green","yellow"]
        let color_hexes = color_variables.map((value,index)=>{
            return getComputedStyle(document.documentElement)
                        .getPropertyValue("--"+value);
        })
        let current_color = color_hexes[index % color_hexes.length]

        return (
        <SkeletonTheme color="#000000" highlightColor="#0f0f0f">
            <div className="card shadow bg-secondary border-0 text-dark text-center m-5" style={{width:"400px"}}>
                <div className="border-bottom-0 card-header bg-white position-relative" >
                    <Skeleton width="100%" height="256px"/>
                    <div className=" absolute-side-right" style={{backgroundColor:current_color,height:"100%",width:"10px"}}>
                    </div>
                </div>
                <div className="card-body position-relative">
                    <h3 className="card-title"><Skeleton/></h3>
                    <hr/>
                    <p className="card-text mb-5"><Skeleton count={3}/></p>
                    <a className="btn absolute-bottom-right disabled" style={{backgroundColor:current_color,borderRadius:"0",borderColor:color_hexes[index]}}><i className="fas fa-chevron-right"></i></a>
                </div>
            </div>
        </SkeletonTheme>
        )
    }
}

export default LinkCardBlockPlaceholder;