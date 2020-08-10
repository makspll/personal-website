import React from 'react';
import Skeleton from 'react-loading-skeleton';
import {sample} from '../js/utils';

class ArticleListingPlaceholder extends React.Component{
   

    render(){
        let widths = [
            "calc(80% - 150px) ",
            "calc(80% - 50px) ",
            "calc(80% - 10px) "]
    
        let no_paragraphs = 4;
        let final_widths = sample(widths,no_paragraphs);


        let paragraphs = final_widths.map((val,index)=>{
            return <p><Skeleton width={val}/></p>
        });
    
        return (
            <div className="article-listing-article pt-5 position-relative text-left pt-3" >
                <h2 className="mb-0"><Skeleton/></h2>
                <div >
                    <div className="text-muted h6">

                        <span><i className="far fa-clock fa-sm" aria-hidden="true"></i></span>
                        <span> <Skeleton width={60}/></span>
                        <br/>
                    </div>
                </div>
                <Skeleton height="400px" className="mb-1 article-listing-thumbnail img-thumbnail"/>
                {paragraphs}
                <hr className="mb-0"/>

            </div>
        )
    }
}

export default ArticleListingPlaceholder;