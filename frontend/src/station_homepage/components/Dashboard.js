import MyChart from "../../shared/components/Charts";

function Dashboard(){
  const data_frame = [
    {
      air_temp: 16,
    },
    {
      air_temp: 17,
    },
    {
      air_temp: 18,
    },
    {
      air_temp: 15,
    },
    {
      air_temp: 12,
    },
  ];

  return(
    <MyChart data={data_frame} />
  );
};

export default Dashboard;