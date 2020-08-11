import React from 'react';
import LinkCardBlock from './LinkCardBlock';
import Spinner from '../component_placeholders/Spinner';

class LinkCardListingBlock extends React.Component{

    render(){
        let {json,isLoaded,index} = this.props;
        let content = null;
        if(isLoaded && json){
            content = 
                <div className="overflow-full-width bg-primary d-flex flex-row justify-content-around flex-wrap align-items-stretch">
                    {json.value.link_cards.map((value,index)=>{
                        return <LinkCardBlock index={index} isLoaded={true} key={index} json={value}/>
                    })}
                </div>
        } else if(isLoaded){
            content = 
                <div className="overflow-full-width bg-primary d-flex flex-row justify-content-around flex-wrap align-items-stretch">
                    <p>Could not load data. Please refresh the page.</p>
                </div>
        } else {
            content =                 
            <div className="overflow-full-width bg-primary d-flex flex-row flex-grow-1 justify-content-around flex-wrap align-items-stretch">
                <Spinner/>
                asdasd
            </div>;
        }
        return content;
    }
}

export default LinkCardListingBlock;