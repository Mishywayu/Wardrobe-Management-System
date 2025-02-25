<template>
<div class="main-container">
    <!-- form -->
  <div class="form-container">
    <h1>Welcome to your Wardrobe!</h1>
    <h2>Register Here</h2>
    <form>
      <div class="form-group">
        <label for="">Name</label>
        <input id="name" type="text" />
      </div>

      <div class="form-group">
        <label for="">Email</label>
        <input id="email" type="email" />
      </div>

      <div class="form-group">
        <label for="">Password</label>
        <input id="password" type="password" />
      </div>

      <div class="form-group">
        <label for="">Confirm Password</label>
        <input id="confirmPassword" type="password" />
      </div>

      <button type="submit">Register</button>
      <p>Already have an account? <span>Login</span></p>
    </form>
  </div>

  <!-- image -->
   <div class="image-container">
   </div>
</div>
</template>

<!-- CSS STYLING -->
<style>
.main-container{
    margin: 0px 300px;
    display: flex;
    width: 60%;
    gap: 4px;
    box-shadow: 0px 1px 10px rgba(0, 0, 0, 0.2);
    border-radius: 5px 0px 0px 5px;
}
.form-container {
    width: 50%;
    padding: 10px;
}
.form-container h1 {
    color: #DAA06D;
    font-size: 30px;
    font-family: 'Times New Roman', Times, serif;
}

.form-container h2 {
    font-family: Georgia, 'Times New Roman', Times, serif;
    font-size: 18px;
    font-weight: lighter;
}

.form-group input {
    width: 95%;
    height: 30px;
    border: 1px solid gray;
    margin: 5px 0px;
}

.form-group label{
    font-family: Georgia, 'Times New Roman', Times, serif;
    font-size: 13px;
}

form button {
    background-color: black;
    color: white;
    width: 97%;
    padding: 10px 10px;
    margin-top: 20px;
}

form button:hover {
    background-color: #DAA06D;
    color: black;
    border: none;
}

form p {
    text-align: center;
}

form p span {
    color: #DAA06D;
}

.image-container{
    background: url('/images/register.jpg'); 
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    background-color: brown;
    width:50%;
}
</style>
