import FreeformListingBlock from './components/FreeformListingBlock';
import React from 'react';
import ReactDOM from 'react-dom';
import './css/all.scss';
import AOS from 'aos';
import 'bootstrap';
import './js/common.js';
import 'popper.js';
ReactDOM.render(
    <FreeformListingBlock />,
    document.getElementById('freeform_content')
    );


AOS.init();
