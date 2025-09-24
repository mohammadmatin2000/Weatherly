import React from 'react';
import './CityInput.css';

export default class CityInput extends React.Component {
  render() {
    const onKlickHandler = async (e) => {
      e.persist();
      const eventKey = e.which ? e.which : e.keyCode;
      const city = e.target.value.trim();

      // وقتی کلید Enter زده شد
      if (eventKey === 13) {
        // بررسی اینکه فقط حروف فارسی یا انگلیسی وارد شده باشد
        if (/^[a-zA-Z\u0600-\u06FF ]+$/.test(city)) {
          e.target.classList.add('loading');

          // فراخوانی API
          const success = await this.props.makeApiCall(city);
          if (success) {
            e.target.placeholder = 'نام شهر را وارد کنید...';
          } else {
            e.target.placeholder = 'شهر یافت نشد، دوباره تلاش کنید...';
          }
        } else {
          e.target.placeholder = 'لطفاً نام شهر معتبر وارد کنید...';
        }

        e.target.classList.remove('loading');
        e.target.value = '';
      }
    };

    const style = {
      top: this.props.city ? '-380px' : '-20px',
      width: '600px',
      display: 'inline-block',
      padding: '10px 0px 10px 30px',
      lineHeight: '120%',
      position: 'relative',
      borderRadius: '20px',
      outline: 'none',
      fontSize: '20px',
      transition: 'all 0.5s ease-out'
    };

    return (
      <input
        className='city-input'
        style={style}
        type='text'
        placeholder='نام شهر را وارد کنید...'
        onKeyPress={onKlickHandler}
      />
    );
  }
}
