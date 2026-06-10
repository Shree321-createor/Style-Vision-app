interface KeywordInputProps {
  onSearch: (
    value: string
  ) => void;
}

function KeywordInput({
  onSearch
}: KeywordInputProps) {

  return (
    <input
      type="text"
      placeholder="Search catalog..."
      style={{
        width: "300px",
        padding: "10px",
        marginBottom: "20px"
      }}
      onChange={(e) =>
        onSearch(
          e.target.value
        )
      }
    />
  );
}

export default KeywordInput;
