export default function Message({
  text,
  type,
}: {
  text: string;
  type: "user" | "bot";
}) {
  return (
    <div className={`p-2 ${type === "user" ? "text-right" : "text-left"}`}>
      <span
        className={`p-2 rounded-md ${
          type === "user" ? "bg-blue-500 text-white" : "bg-gray-300"
        }`}
      >
        {text}
      </span>
    </div>
  );
}
