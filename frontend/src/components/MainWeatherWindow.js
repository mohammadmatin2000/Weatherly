import React from 'react';
import './MainWeatherWindow.css';

// نمایش وضعیت هوا برای روز جاری
export default class MainWeatherWindow extends React.Component {
  // تبدیل روز هفته به فارسی
  getPersianDay = date => {
    const weekdays = ['یکشنبه','دوشنبه','سه‌شنبه','چهارشنبه','پنج‌شنبه','جمعه','شنبه'];
    return weekdays[new Date(date).getDay()];
  }

  // ترجمه وضعیت هوا به فارسی
  translateWeather = desc => {
    const map = {
      'clear sky': 'آسمان صاف',
      'few clouds': 'کمی ابری',
      'scattered clouds': 'ابری پراکنده',
      'broken clouds': 'ابری با شکاف',
      'shower rain': 'باران رگباری',
      'rain': 'باران',
      'thunderstorm': 'رعد و برق',
      'snow': 'برف',
      'mist': 'مه',
      'light rain': 'باران سبک'
    };
    return map[desc] || desc;
  }

  render() {
    const Title = this.props.city ? null : <h1 className='title'>پیش‌بینی هوا</h1>;

    return (
      <div className='main'>
        <div className='inner-main'>
          {Title}
          <img
            src={
              this.props.data
                ? require(`../images/${this.props.data.icon}.svg`)
                : require('../images/01d.svg')
            }
            alt='weather'
            style={{
              visibility: this.props.city ? 'visible' : 'hidden',
              opacity: this.props.city ? '1' : '0'
            }}
          />

          <div
            className='today'
            style={{
              visibility: this.props.city ? 'visible' : 'hidden',
              opacity: this.props.city ? '1' : '0'
            }}
          >
            <span>امروز</span>
            <h1>{this.props.city}</h1>
            <p>دما: {this.props.data ? Math.round(this.props.data.temp) : 0}°C</p>
            <p>{this.props.data ? this.translateWeather(this.props.data.weather_desc) : ''}</p>
          </div>
        </div>
        {this.props.children}
      </div>
    );
  }
}
