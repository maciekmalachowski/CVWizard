import React from "react";

interface LoadingStateProps {
  progress?: number;
}

export function LoadingState({ progress }: LoadingStateProps) {
  return (
    <div className="bg-white/80 backdrop-blur-sm rounded-xl shadow-lg p-6 text-center border border-indigo-100">
      {/* Animated Spinner Icon */}
      <div className="relative mx-auto mb-4 h-12 w-12">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600"></div>

        {/* Percentage Label */}
        {progress !== undefined && progress > 0 && (
          <div className="absolute inset-0 flex items-center justify-center">
            <span className="text-xs font-medium text-indigo-600">
              {Math.round(progress)}%
            </span>
          </div>
        )}
      </div>

      {/* Informative Message */}
      <p className="text-slate-600">Working some AI magic on your CV...</p>

      {/* Progress Bar */}
      {progress !== undefined && progress > 0 && (
        <div className="mt-2 w-full bg-slate-200 rounded-full h-1.5">
          <div
            className="bg-indigo-600 h-1.5 rounded-full transition-all duration-300"
            style={{ width: `${progress}%` }}
          ></div>
        </div>
      )}
    </div>
  );
}
