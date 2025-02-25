<template>
  <div class="outer">
    <div class="inner">
      <h1>Welcome Back!</h1>
      <h2>Login to Your Wardrobe</h2>

      <form>
        <div class="form-group">
          <label for="email">Email</label>
          <input id="email" type="email" />
        </div>

        <div class="form-group">
          <label for="password">Password</label>
          <input id="password" type="password" />
        </div>

        <button type="submit">Login</button>
        <p>Don't have an account? <span>Register</span></p>
      </form>
    </div>
  </div>
</template>


<!-- CSS STYLING -->
<style>
.outer {
  display: flex;
  align-items: center;
  justify-content: center;
}

.inner {
  width: 25%;
  margin-top: 30px;
  padding: 20px;
  box-shadow: 0px 1px 10px rgba(0, 0, 0, 0.2);
  border-radius: 5px;
}

.inner h1 {
  color: #DAA06D;
  font-size: 30px;
  font-family: 'Times New Roman', Times, serif;
}

.inner h2 {
  font-family: Georgia, 'Times New Roman', Times, serif;
  font-size: 18px;
  font-weight: lighter;
}

form input {
  width: 95%;
  height: 35px;
  border: 1px solid gray;
  margin: 5px 0px;
  padding: 5px;
}

form label {
  font-family: Georgia, 'Times New Roman', Times, serif;
  font-size: 13px;
}

form button {
  background-color: black;
  color: white;
  width: 97%;
  padding: 10px;
  margin-top: 20px;
  border: none;
  cursor: pointer;
  font-size: 16px;
}

form button:hover {
  background-color: #DAA06D;
  color: black;
  border: none;
}

form p {
  text-align: center;
  font-size: 14px;
  margin-top: 10px;
}

form p span {
  color: #DAA06D;
  cursor: pointer;
  font-weight: bold;
}
</style>