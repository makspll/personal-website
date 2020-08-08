import React from 'react';


class EventBlock extends React.Component{
    componentDidMount(){
        AOS.refreshHard();
    }
    render(){
        let {isLoaded,json, event_idx, } = this.props;

        let content = null;
        if (isLoaded){
            let aos_vals = ["fade-right","fade-left"]
            content =
                <div className="event py-5" 
                    data-aos={aos_vals[event_idx % 2].toString()}>

                    <span className="event-icon"></span>

                    {json.value.date ? 
                        <span className="year">{ json.value.date }</span>:
                        null}
                    
                    <div className="event-content">
                        <h3 className="title h4 font-weight-bold">{json.value.header}</h3>
                        <p className="description" dangerouslySetInnerHTML={{__html:json.value.lead_paragraph}}></p>
                    </div>
                </div>

              
        }else {
            content = null;
        }
        return content;
    }
}

export default EventBlock;