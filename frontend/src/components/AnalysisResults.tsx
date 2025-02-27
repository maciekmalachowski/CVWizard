import React from "react";
import { Check, X, ChevronRight, Sparkles } from "lucide-react";
import { RadialBarChart, RadialBar, ResponsiveContainer } from "recharts";
import parse from 'html-react-parser';

interface AnalysisResultsProps {
  aiInsights: Record<string, any>;
}

export function AnalysisResults({ aiInsights }: AnalysisResultsProps) {
  // Extract meaningful insights
  const alignmentScore = aiInsights.alignmentScore || 0;
  const calculatedEndAngle = 90 - (360 * alignmentScore) / 100;
  const matchedKeywords = aiInsights.matchedKeywords || [];
  const missingKeywords = aiInsights.missingKeywords || [];
  const suggestions = aiInsights.suggestions || "";

  const data = [
    {
      name: "Alignment",
      value: alignmentScore,
      fill: "url(#colorfulGradient)",
    },
  ];

  return (
    <div className="bg-white/80 backdrop-blur-sm rounded-xl shadow-lg p-6 space-y-6 border border-indigo-100">
      <h2 className="text-2xl font-semibold mb-6 flex items-center space-x-2">
        <Sparkles className="w-6 h-6 text-indigo-600" />
        <span className="bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-600 text-transparent bg-clip-text">
          Magic Results
        </span>
      </h2>
      <div className="grid md:grid-cols-2 gap-6">
        {/* Alignment Score */}
        <div className="bg-gradient-to-br from-indigo-50 to-purple-50 rounded-xl p-4">
          <h3 className="text-lg font-medium mb-4 text-slate-700">
            CV-Job Alignment Score
          </h3>

          {/* Wrapper for Chart and Centered Text */}
          <div className="relative h-48 flex items-center justify-center">
            {/* Radial Chart */}
            <ResponsiveContainer width="100%" height="100%">
              <RadialBarChart
                cx="50%"
                cy="50%"
                innerRadius="60%"
                outerRadius="80%"
                barSize={10}
                data={data}
                startAngle={90}
                endAngle={calculatedEndAngle}
              >
                <defs>
                  <linearGradient id="colorfulGradient" x1="0" y1="0" x2="1" y2="1">
                    <stop offset="0%" stopColor="#4f46e5" />
                    <stop offset="50%" stopColor="#9333ea" />
                    <stop offset="100%" stopColor="#db2777" />
                  </linearGradient>
                </defs>
                <RadialBar background dataKey="value" cornerRadius={30} />
              </RadialBarChart>
            </ResponsiveContainer>

            {/* Centered Percentage Text */}
            <div className="absolute flex items-center justify-center">
              <span className="text-3xl font-bold bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-600 text-transparent bg-clip-text">
                {alignmentScore}%
              </span>
            </div>
          </div>
        </div>


        {/* Keyword Matching */}
        <div className="space-y-4">
          <div>
            <h3 className="text-lg font-medium mb-2 text-slate-700">
              Matched Keywords
            </h3>
            <div className="flex flex-wrap gap-2">
              {matchedKeywords.length > 0 ? (
                matchedKeywords.map((keyword: string) => (
                  <span
                    key={keyword}
                    className="inline-flex items-center px-3 py-1 rounded-full text-sm bg-gradient-to-r from-emerald-50 to-teal-50 text-emerald-700 border border-emerald-200"
                  >
                    <Check className="w-4 h-4 mr-1" />
                    {keyword}
                  </span>
                ))
              ) : (
                <p className="text-slate-500">No matched keywords.</p>
              )}
            </div>
          </div>
          <div>
            <h3 className="text-lg font-medium mb-2 text-slate-700">
              Missing Keywords
            </h3>
            <div className="flex flex-wrap gap-2">
              {missingKeywords.length > 0 ? (
                missingKeywords.map((keyword: string) => (
                  <span
                    key={keyword}
                    className="inline-flex items-center px-3 py-1 rounded-full text-sm bg-gradient-to-r from-red-50 to-rose-50 text-red-700 border border-red-200"
                  >
                    <X className="w-4 h-4 mr-1" />
                    {keyword}
                  </span>
                ))
              ) : (
                <p className="text-slate-500">No missing keywords.</p>
              )}
            </div>
          </div>
        </div>
      </div>

      {/* AI-Powered Suggestions */}
      <div className="mt-6">
        <h3 className="text-lg font-medium mb-4 text-slate-700">
          AI-Powered Suggestions
        </h3>
        <div className="space-y-3">
          <div className="p-4 bg-gradient-to-r from-indigo-50/80 to-purple-50/80 rounded-lg">
            <div className="flex items-start space-x-2">
              <ChevronRight className="w-5 h-5 text-indigo-600 mt-0.5" />
              <div className="markdown-content text-slate-700">
              {parse(suggestions)}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
