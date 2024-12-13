import axios from 'axios';

async function getNestedData() {
  try {
    // Make the first API call
    const usersResponse = await axios.get('https://jsonplacehor.typicode.com/users'); // Example API
    const users = usersResponse.data;

    // Array to hold all profile data
    const allProfileData = [];

    // Iterate through users and fetch profile data
    for (const user of users) { // Using a for...of loop for better error handling within the loop
      try {
        const profileResponse = await axios.get(`https://jsonplaceholder.typicode.com/users/${user.id}/posts`); // Example nested data (posts)
        allProfileData.push({ user: user.name, posts: profileResponse.data });
      } catch (profileError) {
        // Handle errors for individual user profiles gracefully
        console.error(`Error fetching profile for user ${user.id}:`, profileError.message);
        // Add a placeholder or default data if the profile fetch fails
        allProfileData.push({ user: user.name, posts: [] , error: profileError.message}); // Indicate the error
        //Or, continue to the next user without adding any data for the failed user:
        //continue;
      }
    }
    return allProfileData;
  } catch (usersError) {
    // Handle the error from the initial users fetch
    console.error('Error fetching users:', usersError.message);
    //You could return a default value or re-throw the error depending on your needs.
    return {error: usersError.message}; // Return an object indicating the error
    // throw usersError; // Re-throw the error if you want it to propagate up
  }
}

async function displayData() {
  const nestedData = await getNestedData();

  if (nestedData.error) {
    console.error("An error occurred:", nestedData.error)
  } else {
    nestedData.forEach(item => {
        if(item.error){
            console.log(`User: ${item.user} - Error: ${item.error}`)
        }
        else{
            console.log(`User: ${item.user} - Posts: ${item.posts.length}`);
        }

    })
  }

}

displayData();
