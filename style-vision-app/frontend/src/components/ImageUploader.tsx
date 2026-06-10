import axios from "axios";

interface ImageUploaderProps {
  onUploadDone: () => void;
}

function ImageUploader({
  onUploadDone
}: ImageUploaderProps) {

  const handleFileChange = async (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {

    const file = event.target.files?.[0];

    if (!file) {
      return;
    }

    const formPayload = new FormData();

    formPayload.append(
      "image",
      file
    );

    try {

      await axios.post(
        "http://localhost:8000/items/upload",
        formPayload
      );

      alert("Image uploaded successfully");

      onUploadDone();

    } catch (err) {

      console.error(err);

      alert("Upload failed");
    }
  };

  return (
    <div style={{ marginBottom: "20px" }}>
      <input
        type="file"
        accept="image/*"
        onChange={handleFileChange}
      />
    </div>
  );
}

export default ImageUploader;
