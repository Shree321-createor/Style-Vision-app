import type { ClothingItem } from "../types/ClothingItem";

interface CardProps {
  item: ClothingItem;
}

function ClothingCard({ item }: CardProps) {

  return (
    <div
      style={{
        border: "1px solid #ddd",
        borderRadius: "8px",
        padding: "15px",
        backgroundColor: "#fff",
        boxShadow: "0 2px 8px rgba(0,0,0,0.1)"
      }}
    >
      <img
        src={`http://localhost:8000/${item.image_path}`}
        alt={item.garment_type}
        style={{
          width: "100%",
          height: "250px",
          objectFit: "cover",
          borderRadius: "8px"
        }}
      />

      <h3>{item.garment_type}</h3>

      <p>{item.description}</p>

      <p>
        <strong>Style:</strong> {item.style}
      </p>

      <p>
        <strong>Color Palette:</strong> {item.color_palette}
      </p>

      <p>
        <strong>Season:</strong> {item.season}
      </p>

      <p>
        <strong>Occasion:</strong> {item.occasion}
      </p>

      <p>
        <strong>Consumer:</strong> {item.consumer_profile}
      </p>

      <p>
        <strong>Material:</strong> {item.material}
      </p>
    </div>
  );
}

export default ClothingCard;
