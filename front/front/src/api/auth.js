import axios from 'axios';

const API_URL = 'http://localhost:8000/user';


export const registerApi = async (studentNumber, name, password) => {
    try {
        const response = await axios.post(`${API_URL}/register/`, { studentNumber, name, password });
        return response.data;
    } catch (error) {
        throw new Error(error.response.data.message);
    }
};
