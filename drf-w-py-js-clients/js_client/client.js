window.onload = async function () {
  sessionStorage.removeItem("query");
  await validateJWTToken();
};

const contentContainer = document.getElementById("content-container");
const loginForm = document.getElementById("login-form");
const searchForm = document.getElementById("search-form");
const searchInput = document.getElementById("search-input");
const usernameInput = document.getElementById("username-input");
const passwordInput = document.getElementById("password-input");
const baseEndpoint = "http://localhost:8000/api";
if (loginForm) {
  loginForm.addEventListener("submit", handleLogin);
}

if (searchForm) {
  searchForm.addEventListener("submit", handleSearch);
}

function handleLogin(event) {
  event.preventDefault(); 
  const loginEndpoint = `${baseEndpoint}/token/`;
  let loginFormData = new FormData(loginForm);
  let loginObjectData = Object.fromEntries(loginFormData);

  let bodyStr = JSON.stringify(loginObjectData);
  const words = ["hello", "world", "javascript"];
  const wordLengths = Object.fromEntries(
    words.map((word) => [word, word.length])
  );

  
  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: bodyStr,
  };
  fetch(loginEndpoint, options) // Promise
    .then(
      function onfulfilled(response) {
        if (!response.ok) {
          throw new Error("HTTP error, status = " + response.status);
        }
        return response.json();
        
      },
      function onrejected(error) {
        
      }
    )
    .then((authData) => {
      handleAuthData(authData, getProductList);
      usernameInput.value = "";
      passwordInput.value = "";
      sessionStorage.removeItem("event");
      sessionStorage.removeItem("query");
    })
    .catch((err) => {
      
    });
}

function queryGetter() {
  return JSON.parse(sessionStorage.getItem("query"));
}

function accessGetter() {
  return localStorage.getItem("access");
}

function cleanLocal() {
  localStorage.removeItem("access");
  localStorage.removeItem("refresh");
}

async function handleSearch(event, query) {
  event && event.preventDefault(); 
  let searchParams;
  if (query === undefined) {
    let searchFormData = new FormData(searchForm);
    let searchObjectData = Object.fromEntries(searchFormData);

    searchParams = new URLSearchParams(searchObjectData);
    sessionStorage.setItem("query", JSON.stringify(`${searchParams}`));

  } else {
    searchParams = query;
  }
  const searchEndpoint = `${baseEndpoint}/search/?${searchParams}`;

  const headers = {
    "Content-Type": "application/json",
  };
  const authToken = accessGetter();
  if (authToken) {
    headers["Authorization"] = `Bearer ${authToken}`;
  }
  const options = {
    method: "GET",
    headers: headers,
  };
  fetch(searchEndpoint, options) 
    .then(
      function onfulfilled(response) {
        return response.json();
      },
      function onrejected(error) {
      }
    )
    .then(async (searchData) => {
      
      const queryStorage = queryGetter();
      const isValidToken =
        queryStorage && (await validateJWTToken(event, queryStorage));

      if (isValidToken) {
        contentContainer.innerHTML = "";
        if (searchData) {
          for (const [indexName, indexObj] of Object.entries(searchData)) {
            contentContainer.innerHTML += "<p>" + indexName + "</p>" + "<hr/>";
            if (indexObj.hits.length === 0) {
              contentContainer.innerHTML += "<p>No results found</p>";
            }
            let htmlStr = "";
            for (let result of indexObj.hits) {
              htmlStr += "<li>" + result.title + "</li>";
            }
            contentContainer.innerHTML += htmlStr;
          }
        } else {
          contentContainer.innerHTML = "<p>No results found</p>";
        }
      } else {
        contentContainer.innerHTML = "";
        searchInput.value = "";
      }
    })
    .catch((err) => {
      
      searchInput.value = "";
    });
}

function handleAuthData(authData, callback) {
  localStorage.setItem("access", authData.access);
  localStorage.setItem("refresh", authData.refresh);
  callback && callback();
}

function writeToContainer(data) {
  if (contentContainer) {
    contentContainer.innerHTML =
      "<pre>" + JSON.stringify(data, null, 4) + "</pre>";
  }
}

function isTokenValid(jsonData) {
  if (jsonData?.code && jsonData.code === "token_not_valid") {
    refreshToken(getProductList);
    return false; 
  return true; 
}

function getFetchOptions(method, jsObject) {
  return {
    method: method === undefined ? "GET" : method,
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${accessGetter()}`,
    },
    body: jsObject ? JSON.stringify(jsObject) : null,
  };
}

function getProductList() {
  const endpoint = `${baseEndpoint}/products/`;
  const options = getFetchOptions();
  fetch(endpoint, options)
    .then((response) => response.json())
    .then((data) => {
      if (isTokenValid(data)) {
        writeToContainer(data);
      }
    });
}

async function refreshToken(retryCallback) {
  console.log('Refreshing access token...');
  const query = queryGetter();

  const refreshStorage = localStorage.getItem("refresh");

  if (refreshStorage) {
    const refreshEndpoint = `${baseEndpoint}/token/refresh/`;

    const refreshData = {
      refresh: refreshStorage,
    };

    const refreshOptions = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(refreshData),
    };

    try {
      const response = await fetch(refreshEndpoint, refreshOptions);

      const refreshResponse = await response.json();
      

      if (refreshResponse.access) {
        console.log('Access token has been successfully refreshed.');
        localStorage.setItem("access", refreshResponse.access);
        if (typeof retryCallback === "function") {
          retryCallback();
        }
        if (typeof query === "string") {
          await handleSearch(undefined, query);
        }
        return true;
      } else {
        cleanLocal();
        contentContainer.innerHTML = "";
        retryCallback && alert("Session expired. Please login again.");
        

        return false;
      }
    } catch (error) {
      return false;
      console.log('Refreshing error: ', error);  
    }
  }

  return false;
}


async function validateJWTToken() {
  // fetch
  const accessToken = accessGetter();
  const query = queryGetter();
  
  if (accessToken) {
    const query = queryGetter();
    
    const validateEndpoint = `${baseEndpoint}/token/verify/`;
    const validateOptions = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ token: accessToken }),
    };
    try {
      const response = await fetch(validateEndpoint, validateOptions);
      const validateResponse = await response.json();
      
      if (validateResponse.code === "token_not_valid") {
        const refreshSuccess = await refreshToken();
        
        const accessToken = accessGetter();
        
        if (!accessToken) {
          cleanLocal();
          contentContainer.innerHTML = "";

          alert("Session expired. Please login again.");
          
          return false;
        }
      }
      if (!query) {
        getProductList();
      }
      return true;
    } catch (error) {
      return false;
    }
  } else {
    alert("Access token not found, please login.");

    return false;
  }
}

