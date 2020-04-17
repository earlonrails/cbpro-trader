import React from 'react';
import { VictoryCandlestick, VictoryChart, VictoryAxis, VictoryLabel, VictoryTheme } from 'victory';

function Chart (props) {
    const { active_period, candlesticks } = props;
    const victoryLabelStyle = {
      fontWeight: "bold",
      fontSize: 20,
      fill: "rgb(217, 217, 217)"
    }
    const tickAxisStyle = {
      tickLabels: {
        fill: "rgb(217, 217, 217)"
      }
    }
    const candleColors = { positive: "#53b987", negative: "#eb4d5c" }

    const tickFormatter = (t) => {
      const format = {
        year: "2-digit",
        month: "numeric",
        day: "numeric",
        hour: "numeric",
        minute: "numeric",
        hourCycle: "h24"
      }
      return `${t.toLocaleString(undefined, format).replace(',', '\n')}`
    }

    return (
        <div id="chart">
            <VictoryChart
                theme={VictoryTheme.material}
                domainPadding={{ x: 15 }}
                height={600}
                width={1000}
                scale={{ x: "time"}}
            >
                <VictoryLabel text={active_period} x={20} y={20} style={victoryLabelStyle}/>
                <VictoryAxis
                    tickFormat={tickFormatter}
                    tickCount={25}
                    style={tickAxisStyle}
                />
                <VictoryAxis
                    dependentAxis
                    style={tickAxisStyle}
                />
                <VictoryCandlestick
                candleColors={candleColors}

                data={candlesticks.slice(candlesticks.length-50, candlesticks.length)}
                x={(d) => Date.parse(d[0])}
                open={3}
                close={4}
                high={2}
                low={1} />
            </VictoryChart>
        </div>
    )
}

export default Chart;