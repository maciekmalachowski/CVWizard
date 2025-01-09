import React, { useState } from "react";
import {
  Upload,
  Link,
  AlertCircle,
  Check,
  Wand2,
} from "lucide-react";
import { useDropzone } from "react-dropzone";
import { AnalysisResults } from "./components/AnalysisResults";
import { LoadingState } from "./components/LoadingState";
import { analyzeCV, AnalysisResponse } from './services/api';


export function App() {
  const [file, setFile] = useState<File | null>(null);
  const [url, setUrl] = useState("");
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [results, setResults] = useState<AnalysisResponse | null>(null);
  const [error, setError] = useState("");
  const [uploadProgress, setUploadProgress] = useState(0);

  const onDrop = (acceptedFiles: File[]) => {
    if (acceptedFiles.length > 0) {
      setFile(acceptedFiles[0]);
      setError("");
      setUploadProgress(0);
    }
  };

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      "application/pdf": [".pdf"],
      "application/msword": [".doc"],
      "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        [".docx"],
    },
    maxFiles: 1,
  });

  const handleAnalyze = async () => {
    if (!file || !url) {
      setError("Please provide both a CV and a job URL");
      return;
    }
    try {
      setIsAnalyzing(true);
      setError("");
      const result = await analyzeCV(file, url);
      setResults(result);
    } catch (err) {
      setError(
        err instanceof Error ? err.message : "An unexpected error occurred",
      );
    } finally {
      setIsAnalyzing(false);
    }
  };
  
  return (
    <main className="min-h-screen w-full bg-gradient-to-br from-indigo-50 via-purple-50 to-pink-50 p-4 sm:p-6 md:p-8">
      <div className="max-w-4xl mx-auto space-y-6">
        <header className="text-center mb-8">
          <div className="inline-flex items-center justify-center space-x-3 mb-4">
            <Wand2 className="w-10 h-10 text-indigo-600" />
            <h1 className="text-4xl font-bold bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-600 text-transparent bg-clip-text">
              CVWizard
            </h1>
          </div>
          <p className="text-slate-600">
            Transform your CV into the perfect match for your dream job using AI
            magic
          </p>
        </header>
        <div className="bg-white/80 backdrop-blur-sm rounded-xl shadow-lg p-6 space-y-6 border border-indigo-100">
          <div>
            <h2 className="text-xl font-semibold mb-4 text-slate-800 flex items-center">
              <span className="bg-gradient-to-r from-indigo-500 to-purple-500 text-white w-7 h-7 rounded-full flex items-center justify-center text-sm mr-2">
                1
              </span>
              Upload your CV
            </h2>
            <div
              {...getRootProps()}
              className={`border-2 border-dashed rounded-xl p-8 text-center cursor-pointer transition-all duration-300
                ${isDragActive ? "border-indigo-500 bg-indigo-50" : "border-slate-200 hover:border-indigo-400 hover:bg-indigo-50/50"}`}
            >
              <input {...getInputProps()} />
              <Upload
                className={`mx-auto h-12 w-12 mb-4 ${isDragActive ? "text-indigo-600" : "text-indigo-500"}`}
              />
              <p className="text-slate-600">
                {isDragActive
                  ? "Drop your CV here"
                  : "Drag and drop your CV, or click to select"}
              </p>
              <p className="text-sm text-slate-500 mt-2">
                Supported formats: PDF, DOC, DOCX
              </p>
            </div>
            {file && (
              <p className="mt-2 text-sm text-emerald-600 flex items-center">
                <Check className="w-4 h-4 mr-1" />
                Selected file: {file.name}
              </p>
            )}
          </div>
          <div>
            <h2 className="text-xl font-semibold mb-4 text-slate-800 flex items-center">
              <span className="bg-gradient-to-r from-purple-500 to-pink-500 text-white w-7 h-7 rounded-full flex items-center justify-center text-sm mr-2">
                2
              </span>
              Enter Job URL
            </h2>
            <div className="flex items-center space-x-4">
              <div className="flex-1">
                <input
                  type="url"
                  value={url}
                  onChange={(e) => setUrl(e.target.value)}
                  placeholder="Paste justjoin.it job URL here"
                  className="w-full px-4 py-3 border border-slate-200 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-purple-500 outline-none text-slate-600 placeholder-slate-400"
                />
              </div>
              <Link className="h-6 w-6 text-purple-400" />
            </div>
          </div>
          {error && (
            <div className="flex items-center space-x-2 text-red-600 bg-red-50 p-3 rounded-lg">
              <AlertCircle className="h-5 w-5" />
              <span>{error}</span>
            </div>
          )}
          <button
            onClick={handleAnalyze}
            disabled={isAnalyzing || !file || !url}
            className="w-full bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-600 text-white py-3 rounded-lg font-medium
              hover:from-indigo-500 hover:via-purple-500 hover:to-pink-500 disabled:from-slate-300 disabled:to-slate-300 disabled:cursor-not-allowed
              transition-all duration-300 shadow-sm hover:shadow-md"
          >
            {isAnalyzing ? "Analyzing..." : "Analyze CV"}
          </button>
        </div>
        {isAnalyzing && <LoadingState progress={uploadProgress} />}
        {results && <AnalysisResults results={results} />}
      </div>
    </main>
  );
}
