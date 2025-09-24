import React from "react";
import MainWeatherWindow from "./components/MainWeatherWindow";
import CityInput from "./components/CityInput";
import WeatherBox from "./components/WeatherBox";
import "./App.css";

class App extends React.Component {
  state = {
    city: "",
    days: [],
    loading: false,
    error: ""
  };

  // فراخوانی API داخلی Django
  makeApiCall = async (city) => {
    if (!city) return;

    this.setState({ loading: true, error: "", days: [] });

    try {
      const response = await fetch(`http://127.0.0.1:80/weather/weather/?city=${city}`);
      const data = await response.json();

      if (data.error) {
        this.setState({ error: data.error, loading: false });
        return false;
      }

      this.setState({
        city: data.city,
        days: data.days,
        loading: false
      });

      return true;

    } catch (err) {
      console.error(err);
      this.setState({ error: "Error fetching data", loading: false });
      return false;
    }
  };

  render() {
    const WeatherBoxes = () => (
      <ul className="weather-box-list">
        {this.state.days.slice(1).map((day, index) => (
          <li key={index}>
            <WeatherBox {...day} />
          </li>
        ))}
      </ul>
    );

    return (
      <div className="App">
        <header className="App-header">
          {this.state.loading && <p>Loading...</p>}
          {this.state.error && <p style={{ color: "red" }}>{this.state.error}</p>}

          <MainWeatherWindow
            city={this.state.city}
            data={this.state.days[0]}
          >
            <CityInput
              city={this.state.city}
              makeApiCall={this.makeApiCall.bind(this)}
            />
            <WeatherBoxes />
          </MainWeatherWindow>
        </header>
      </div>
    );
  }
}

export default App;
