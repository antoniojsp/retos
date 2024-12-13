const axios = require('axios');

async function getNestedData() {
  try {
    // Make the first API call
    const firstResponse = await axios.get('https://example.com/api/v1/users');
    const users = firstResponse.data;

    // For each user, make a second API call to get their profile data
    const profileData = await Promise.all(users.map(async (user) => {
      try {
        const secondResponse = await axios.get(`https://example.com/api/v1/users/${user.id}/profile`);
        return secondResponse.data;
      } catch (error) {
        // Handle error for individual user profile request
        console.error(`Failed to get profile data for user ${user.id}:`, error.message);
        return { userId: user.id, error: `Failed to get profile data` };
      }
    }));

    // Return the profile data for all users
    return profileData;

  } catch (error) {
    // Handle error for the first API call
    console.error('Failed to get users:', error.message);
    return { error: 'Failed to get users' };
  }
}

// Get the nested data
getNestedData().then((nestedData) => {
  // Use the nested data
  console.log(nestedData);
}).catch((error) => {
  // Handle any unexpected errors
  console.error('Unexpected error:', error.message);
});