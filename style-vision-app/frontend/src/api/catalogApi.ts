import axios from "axios";

const BASE_URL = "http://localhost:8000";

export const fetchAllItems = async () => {
  const response = await axios.get(
    `${BASE_URL}/items`
  );

  return response.data;
};

export const searchByKeyword = async (
  keyword: string
) => {

  const response = await axios.get(
    `${BASE_URL}/items/search?q=${keyword}`
  );

  return response.data;
};
