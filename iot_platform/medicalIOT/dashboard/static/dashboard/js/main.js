// Deprecated, script no longer used

const getOptionChart=async()=>{

    try{
        const response=await  fetch("http://127.0.0.1:8000/get_chart/");
        return await response.json();
    }catch(ex) {
        alert(ex);
    }

};


// Selector para obtener un elemento por su identificador, en nuestro caso "chart"
// Qué esta en el dashboard
const initChart = async () => {
    const myChart = echarts.init(document.getElementById("chart"));


    myChart.setOption(await getOptionChart());

    myChart.resize();

};

window.addEventListener("load",async()=>{
    await initChart();



});
