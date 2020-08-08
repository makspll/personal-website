import React from 'react';

class RichTextBlock extends React.Component{


    render(){

        return(
            <div className="rich-text text-left" dangerouslySetInnerHTML={{__html:this.props.json.value}}>
            </div>
        )
    }
}

export default RichTextBlock;