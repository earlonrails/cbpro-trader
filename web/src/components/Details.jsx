import React from 'react';

function Details(props) {
    const { indicators } = props;
    const tradeIndicators = Object.keys(indicators).map((indicator) => {
        return(
            <div className="indicator" key={indicators[indicator]}>
                <div className="indicator-title">{indicator.toUpperCase()}</div>
                <div className="indicator-data">{indicators[indicator]}</div>
            </div>
        )
    })
    return(
        <div id="details">
            <div id="last-trade-label">Last Trade</div>
            <div id="last-trade">{indicators.close && indicators.close.toFixed(2)}</div>
            <div id="indicators">
                {tradeIndicators}
            </div>
        </div>
    )
}

export default Details;