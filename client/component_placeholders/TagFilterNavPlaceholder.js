import React from 'react';
import Skeleton, { SkeletonTheme }  from 'react-loading-skeleton';
import {sample, LightenColor} from '../js/utils';

class TagFilterNavPlaceholder extends React.Component{

    render() { 
            let widths = [
                "50px","60px","70px"
            ]
            
            let no_tags = Math.floor((Math.random() * 5)) + 5;
            let final_widths = sample(widths,no_tags);
            let tag_placeholders = [];
            for(let i = 0; i < no_tags;i++){
                tag_placeholders.push(
                        <button className="btn btn-secondary btn-sm p-0 m-1">
                            <Skeleton width={final_widths[i]}  className="mr-1"/>
                        </button>
                    )
            }
            let skeleton_color = getComputedStyle(document.documentElement)
                                    .getPropertyValue('--secondary');
            let highlight_color = LightenColor(skeleton_color,60);
            return ( 
                <nav className="bg-primary text-light border border-gray p-2 overflow-auto">
                    <div className="d-flex">
                        <p className="m-0 text-left h3">Filters</p>

                        <button 
                            className="btn btn-warning btn-sm ml-auto disabled"
                            >
                            Clear Filters
                        </button>

                    </div>
                    <hr className="my-2 bg-light"/>
                    <div className="d-flex flex-row flex-wrap">
                        <SkeletonTheme color={skeleton_color} highlightColor={highlight_color}>
                            <div>
                            {tag_placeholders}
                            </div>
                        </SkeletonTheme>
                    </div>
                </nav>);
}

}

export default TagFilterNavPlaceholder
