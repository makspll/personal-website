import React from 'react';
import LinkCardBlock from './LinkCardBlock';

class LinkCardListingBlock extends React.Component{

    render(){
        let {json,isLoaded,index} = this.props;
        console.log(json);
        let content = null;
        if(isLoaded && json){
            content = 
                <div className="overflow-full-width bg-primary d-flex flex-row justify-content-around flex-wrap align-items-stretch">
                    {json.value.link_cards.map((value,index)=>{
                        return <LinkCardBlock index={index} isLoaded={true} key={index} json={value}/>
                    })}
                </div>
        } else if(isLoaded){
            content = <p>Could not load data. Please refresh the page.</p>
        } else {
            content = null;
        }
        return content;
    }
}

export default LinkCardListingBlock;