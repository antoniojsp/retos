const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
  name: String,
  email: String
}, { timestamps: true });

const User = mongoose.model('User', userSchema);

// Creating a new user
const newUser = new User({ name: 'John Doe', email: 'john.doe@example.com' });
await newUser.save();
// At this point, newUser will have createdAt and updatedAt fields populated

// Updating the user's email
newUser.email = 'new.email@example.com';
await newUser.save();
// Now, the updatedAt field will be updated to the current time
