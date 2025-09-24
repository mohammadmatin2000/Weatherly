import React from 'react';
import './WeatherBox.css';

export default class WeatherBox extends React.Component {
  // تبدیل تاریخ به روز هفته فارسی
  getDay = date => {
    const weekday = ['یکشنبه','دوشنبه','سه‌شنبه','چهارشنبه','پنج‌شنبه','جمعه','شنبه'];
    return weekday[new Date(date).getDay()];
  };

  render() {
    return (
      <div className='weather-box'>
        <h1>{this.props.date ? this.getDay(this.props.date) : ''}</h1>
        <img
          src={
            this.props.icon
              ? require(`../images/${this.props.icon}.svg`)
              : require('../images/01d.svg')
          }
          alt='وضعیت آب و هوا'
        />
        <span className='temp'>{this.props.temp ? Math.round(this.props.temp) : 0}°C</span>
      </div>
    );
  }
}
