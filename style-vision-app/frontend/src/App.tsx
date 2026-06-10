import { useEffect, useState } from "react";

import {
  fetchAllItems,
  searchByKeyword
} from "./api/catalogApi";

import ClothingCard from "./components/ClothingCard";
import KeywordInput from "./components/KeywordInput";
import ImageUploader from "./components/ImageUploader";
import type { ClothingItem } from "./types/ClothingItem";

function App() {

  const [catalog, setCatalog] = useState<ClothingItem[]>([]);

  useEffect(() => {
    loadCatalog();
  }, []);

  const loadCatalog = async () => {
    const data = await fetchAllItems();
    setCatalog(data);
  };

  const handleKeywordSearch = async (
    value: string
  ) => {

    if (!value.trim()) {
      await loadCatalog();
      return;
    }

    const data = await searchByKeyword(value);

    setCatalog(data);
  };

  return (
    <div style={{
      maxWidth: "1400px",
      margin: "0 auto",
      padding: "20px" }}>

      <h1>
        Style Vision Catalog
      </h1>

      <ImageUploader
        onUploadDone={loadCatalog}
      />

      <KeywordInput
        onSearch={handleKeywordSearch}
      />

      <div
        style={{
          display: "grid",
          gridTemplateColumns:
            "repeat(auto-fill, minmax(350px, 1fr))",
          gap: "20px"
        }}
      >
        {catalog.map((item) => (
          <ClothingCard
            key={item.id}
            item={item}
          />
        ))}
      </div>

    </div>
  );
}

export default App;
