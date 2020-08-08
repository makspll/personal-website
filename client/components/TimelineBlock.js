import React from 'react';
import EventBlock from './EventBlock';

class TimelineBlock extends React.Component{
    render(){
        let {isLoaded,json} = this.props;

        let content = null;
        if (isLoaded){
            let events = json.value.timeline_items.map((value,index)=>
                    <EventBlock key={index} isLoaded={true} json={value} event_idx={index}/>
            )
            content = 
                <div className="main-timeline">
                    {events}
                </div>
        }else {
            content = 
                <div className="main-timeline">
                <EventBlock />
                </div>
        }
        return (content);


    }
}

export default TimelineBlock;