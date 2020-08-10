import React from 'react';
import RichTextBlockPlaceholder from '../component_placeholders/RichTextBlockPlaceholder';

class RichTextBlock extends React.Component{


    render(){
        let {isLoaded,json} = this.props;

        if(isLoaded && json){
            return(
                <div className="rich-text text-left" dangerouslySetInnerHTML={{__html:json.value}}>
                </div>
            )
        } else if (isLoaded) {
            return <p>Something went wrong, please refresh the page.</p>
        } else {
            return <RichTextBlockPlaceholder/>;
        }
        
    }
}

export default RichTextBlock;