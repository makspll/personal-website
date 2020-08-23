import React from 'react';
import Skeleton, { SkeletonTheme }  from 'react-loading-skeleton';
import {sample, LightenColor} from '../js/utils';

class TagFilterPlaceholder extends React.Component{

    render() { 
            let widths = [
                "50px","60px","70px"
            ]
            
            let no_tags = Math.floor((Math.random() * 5)) + 5;
            let final_widths = sample(widths,no_tags);
            let tag_placeholders = [];
            for(let i = 0; i < no_tags;i++){
                tag_placeholders.push(
                        <button key={i} className="btn btn-secondary btn-sm p-0 m-1">
                            <Skeleton width={final_widths[i]}  className="mr-1"/>
                        </button>
                    )
            }
            let skeleton_color = getComputedStyle(document.documentElement)
                                    .getPropertyValue('--secondary');
            let highlight_color = LightenColor(skeleton_color,60);
            return ( 
                    <div className="d-flex flex-row flex-wrap">
                        <SkeletonTheme color={skeleton_color} highlightColor={highlight_color}>
                            <div>
                            {tag_placeholders}
                            </div>
                        </SkeletonTheme>
                    </div>)
    }
}

export default TagFilterPlaceholder
