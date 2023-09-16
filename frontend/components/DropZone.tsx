import { FileWithPath, useDropzone } from "react-dropzone";

export const Dropzone = () => {
	const { acceptedFiles, getRootProps, getInputProps, isDragActive } = useDropzone();

	const files = acceptedFiles.map((file: FileWithPath) => (
		<li
			key={file.path}
			style={{
				border: "2px solid gray",
				padding: "10px",
				borderRadius: "4px",
			}}
		>
			{file.path} - {file.size} bytes
		</li>
	));

	return (
		<div>
			<div {...getRootProps()} className="box is-bordered">
				<input {...getInputProps()} />
				{isDragActive ? (
					<p>Drop the files here ...</p>
				) : (
					<p>Drag and drop some files here, or click to select files</p>
				)}
			</div>
			<div>
				<ul>{files}</ul>
			</div>
		</div>
	);
};
