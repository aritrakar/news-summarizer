import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
    const [url, setUrl] = useState('');
    const [summary, setSummary] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const handleSubmit = async (e) => {
      console.log('url:', url)
        e.preventDefault();
        setLoading(true);
        setError('');
        setSummary('');
        
        try {
            const response = await axios.post('http://localhost:5000/summarize', { url },
            { headers: { 'Content-Type': 'application/json' } }
            );
            setSummary(response.data.summary);
        } catch (error) {
            setError('Error summarizing the URL. Please try again.');
        }
        
        setLoading(false);
    };

    return (
        <div className="App">
            <h1>AI-Powered News Summarizer</h1>
            <form onSubmit={handleSubmit}>
                <input 
                    type="text"
                    value={url}
                    onChange={(e) => setUrl(e.target.value)}
                    placeholder="Enter news article URL"
                    required
                />
                <button type="submit">Summarize</button>
            </form>
            {loading && <p>Loading...</p>}
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {summary && (
                <div>
                    <h2>Summary</h2>
                    <p>{summary}</p>
                </div>
            )}
        </div>
    );
}

export default App;
