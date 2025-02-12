import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000';

const api = axios.create({
  baseURL: API_BASE_URL,
});

/**
 * Uploads the CV and retrieves processed insights
 */
export const getCvData = async (file: File): Promise<{ CvData: Record<string, any> }> => {
  const formData = new FormData();
  formData.append('cv', file);

  try {
    const response = await api.post<{ CvData: Record<string, any> }>('/read-cv', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    });

    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      throw new Error(error.response?.data?.error || 'Failed to process CV.');
    }
    throw error;
  }
};


/**
 * Fetches job description data from a given URL
 */
export const getJobData = async (jobUrl: string): Promise<Record<string, any>> => {
  try {
    const response = await api.post('/get-job-data', { url: jobUrl });
    
    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      throw new Error(error.response?.data?.error || 'Failed to retrieve job data.');
    }
    throw error;
  }
};


/**
 * Fetches AI insights from a given CV and Job data
 */

export const getAiInsights = async (cvData: Record<string, any>, jobData: Record<string, any>): Promise<{ insights: Record<string, any> }> => {
  try {
    const payload = {
      cvData,
      jobData
    };

    const response = await api.post<{ insights: Record<string, any> }>('/get-ai-insights', payload, {
      headers: {
        'Content-Type': 'application/json',
      },
    });
    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      throw new Error(error.response?.data?.error || 'Failed to create insights.');
    }
    throw error;
  }
};
