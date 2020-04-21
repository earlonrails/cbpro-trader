import React from 'react'

function Flags(props) {
    const { flags } = props
    const products = Object.keys(flags).map((flag) => {
        return(
            <div className="product" key={flag.toUpperCase() + flags[flag]}>
                <div className="product_name">{flag.toUpperCase()}</div>
                <div className="flag">{flags[flag]}</div>
            </div>
        )
    })

    return(
        <div id="flags">
            {products}
        </div>
    )
}

export default Flags
