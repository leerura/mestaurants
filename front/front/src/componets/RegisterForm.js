import React, { useState } from 'react';
import { registerApi } from '../api/auth';

function RegisterForm() {
  const [studentNumber, setStudentNumber] = useState('');
  const [name, setName] = useState('');
  const [password, setPassword] = useState('');  
   
  const handleRegister = async (e) => {
    e.preventDefault();
    try {
      const response = await registerApi(
        studentNumber,
        name,
        password
      );
      console.log(response);
      alert('회원가입 성공!');
    } catch (error) {
      console.error('Registration failed', error);
      alert('회원가입 실패. 다시 시도하세요.');
    }
  };

  return (
    <form onSubmit={handleRegister}>
      <input
        type="text"
        name="studentNumber"
        onChange={(e) => setStudentNumber(e.target.value)}
        placeholder="학번"
        required
      />
      <input
        type="text"
        name="name"
        onChange={(e) => setName(e.target.value)}
        placeholder="이름"
        required
      />
      <input
        type="password"
        name="password"
        onChange={(e) => setPassword(e.target.value)}
        placeholder="비밀번호"
        required
      />
      <button type="submit">회원가입</button>
    </form>
  );
}

export default RegisterForm;