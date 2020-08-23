import React from 'react';
import {GET_ROOT_URL,GET_API_ROOT_URL} from '../DynamicVariables.js';
import ContentLoader from "react-content-loader"

class CheckboxFilter extends React.Component{



    selectBox(name){
        let {filters} = this.props;
        let new_filters = Object.assign({},this.props.filters);
        new_filters["selected_radiobuttons"] = [...filters.selected_radiobuttons,name];
        this.props.set_filters(new_filters);
    }

    deSelectBox(name){

        let {filters} = this.props;

        let idx_of_tag = filters.selected_radiobuttons.indexOf(name);
        let selected_radiobuttons_copy = filters.selected_radiobuttons.slice();
        selected_radiobuttons_copy.splice(idx_of_tag,1);

        let new_filters = Object.assign({},filters);
        new_filters["selected_radiobuttons"] = selected_radiobuttons_copy

        this.props.set_filters(new_filters)

    }

    handleRadioClick(name,currentState){
        if(currentState){
            this.deSelectBox(name);
        } else {
            this.selectBox(name);
        }
    }

    render() { 
        let {filters} = this.props;
        let buttons = this.props.button_names.map((val,idx)=>{
            let btn_checked = !filters.selected_radiobuttons || 
                        filters.selected_radiobuttons.length !== 0 || 
                        filters.selected_radiobuttons.some((name)=>
                            val === name
                        );
            return (
                <div key={idx} className="radio">
                    <label><input type="checkbox" name="optradio" checked={btn_checked} onChange={()=>this.handleRadioClick(val,btn_checked)}/> {val}</label>
                </div>
            )
            
        });
        
        let content = 
            <div className="d-flex flex-column flex-grow-1 align-items-start ml-1">
                {buttons}
            </div>
        return(content);    
}

}

export default CheckboxFilter
