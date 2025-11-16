export function scoreToGrade(score) {
  const gradeThresholds = [
    { minimum: 9900000, grade: "EX+" },
    { minimum: 9800000, grade: "EX" },
    { minimum: 9500000, grade: "AA" },
    { minimum: 9200000, grade: "A" },
    { minimum: 8900000, grade: "B" },
    { minimum: 8600000, grade: "C" },
  ];

  for (const threshold of gradeThresholds) {
    if (score >= threshold.minimum) {
      return threshold.grade;
    }
  }

  return "D";
}
