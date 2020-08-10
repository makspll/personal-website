import React from 'react';
import Skeleton from 'react-loading-skeleton';
import {sample} from '../js/utils';

class RichTextBlockPlaceholder extends React.Component{


    render(){
        let widths = [
        "calc(100% - 150px) ",
        "calc(100% - 100px) ",
        "calc(100% - 50px) "]

        let paragraphs = 5;
        let final_widths = sample(widths,paragraphs);


        return(
            <div className="rich-text text-left" dangerouslySetInnerHTML={{__html:json.value}}>
                {final_widths.map((val,index)=><Skeleton wdith={val}/>)}
            </div>
        )

    }
}

export default RichTextBlockPlaceholder;