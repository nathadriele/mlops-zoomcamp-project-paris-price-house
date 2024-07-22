'use client';

import Head from 'next/head';
import axios from 'axios';
import { useState } from 'react';

function Home() {
  const [formData, setFormData] = useState({
    squareMeters: '',
    numberOfRooms: '',
    hasYard: '',
    hasPool: '',
    floors: '',
    cityCode: '',
    cityPartRange: '',
    numPrevOwners: '',
    made: '',
    isNewBuilt: '',
    hasStormProtector: '',
    basement: '',
    attic: '',
    garage: '',
    hasStorageRoom: '',
    hasGuestRoom: '',
  });
  const [prediction, setPrediction] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    if (Number(value) >= 0) {
      setFormData(prevState => ({
        ...prevState,
        [name]: value
      }));
    }
  };

  const handlePredict = async () => {
    if (Object.values(formData).every(value => value !== '')) {
      setIsLoading(true);
      try {
        const data = Object.fromEntries(
          Object.entries(formData).map(([key, value]) => [key, Number(value)])
        );

        const response = await axios.post('http://localhost:5000/predict', data);
        if (response.data.predicted_price !== undefined) {
          setPrediction(`Forecasted Price: €${response.data.predicted_price.toFixed(2)}`);
        } else {
          setPrediction('An error occurred while making the forecast. Please try again later.');
        }
      } catch (error) {
        console.error("Error in making the forecast:", error);
        setPrediction('An error occurred while making the forecast. Please try again later.');
      } finally {
        setIsLoading(false);
      }
    } else {
      setPrediction('Please fill in all fields to get a forecast!');
    }
  };

  const handleClear = () => {
    setFormData({
      squareMeters: '',
      numberOfRooms: '',
      hasYard: '',
      hasPool: '',
      floors: '',
      cityCode: '',
      cityPartRange: '',
      numPrevOwners: '',
      made: '',
      isNewBuilt: '',
      hasStormProtector: '',
      basement: '',
      attic: '',
      garage: '',
      hasStorageRoom: '',
      hasGuestRoom: '',
    });
    setPrediction('');
  };

  return (
    <div style={{ margin: '0', padding: '0', minHeight: '100vh' }}>
      <Head>
        <title>Property Price Forecast in Paris</title>
      </Head>
      <h1 style={{ textAlign: 'center', fontSize: '35px', marginTop: '30px', marginBottom: '30px', fontWeight: 'bold' }}>Property Price Forecast in Paris</h1>
      <div style={{ width: '80%', margin: '0 auto', padding: '30px', borderRadius: '10px', boxShadow: '0 0 15px rgba(82, 78, 78, 1)' }}>
        {Object.keys(formData).map((key) => (
          <input
            key={key}
            type="number"
            name={key}
            placeholder={key.charAt(0).toUpperCase() + key.slice(1).replace(/([A-Z])/g, ' $1').trim()}
            value={formData[key as keyof typeof formData]}
            onChange={handleInputChange}
            style={{ margin: '10px', padding: '10px', width: 'calc(50% - 20px)', color: '#00000' }}
            min="0" 
          />
        ))}
        <button 
          onClick={handlePredict} 
          style={{ 
            margin: '40px 10px', 
            padding: '15px', 
            backgroundColor: 'rgb(255, 69, 58)', 
            border: 'none', 
            color: 'white', 
            cursor: 'pointer',
            width: 'calc(100% - 20px)'
          }}
        >
          Estimate Price
        </button>
        <button 
          onClick={handleClear} 
          style={{ 
            margin: '-10px 10px', 
            padding: '15px', 
            backgroundColor: 'rgb(64, 96, 245, 1)', 
            border: 'none', 
            color: 'white', 
            cursor: 'pointer',
            width: 'calc(100% - 20px)'
          }}
        >
          Clear Fields
        </button>
        {isLoading && <div style={{ textAlign: 'center', fontSize: '20px', marginTop: '20px' }}>Loading...</div>}
        <div style={{ textAlign: 'center', fontSize: '20px', marginTop: '20px' }}>{prediction}</div>
      </div>
    </div>
  );
}

export default Home;