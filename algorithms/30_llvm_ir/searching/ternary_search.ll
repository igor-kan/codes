; ModuleID = 'algorithms/02_c/searching/ternary_search.c'
source_filename = "algorithms/02_c/searching/ternary_search.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@.str = private unnamed_addr constant [47 x i8] c"[C TernarySearch] FAILED: argmax %f, want 2.0\0A\00", align 1
@str = private unnamed_addr constant [51 x i8] c"[C TernarySearch] Unimodal maximum verified at x=2\00", align 1

; Function Attrs: nofree norecurse nosync nounwind sspstrong memory(none) uwtable
define dso_local double @ternary_search_max(double noundef %0, double noundef %1, double noundef %2) local_unnamed_addr #0 {
  %4 = fsub double %1, %0
  %5 = fcmp ogt double %4, %2
  br i1 %5, label %6, label %25

6:                                                ; preds = %3, %6
  %7 = phi double [ %23, %6 ], [ %4, %3 ]
  %8 = phi double [ %22, %6 ], [ %0, %3 ]
  %9 = phi double [ %21, %6 ], [ %1, %3 ]
  %10 = fdiv double %7, 3.000000e+00
  %11 = fadd double %8, %10
  %12 = fsub double %9, %10
  %13 = insertelement <2 x double> poison, double %11, i64 0
  %14 = insertelement <2 x double> %13, double %12, i64 1
  %15 = fadd <2 x double> %14, splat (double -2.000000e+00)
  %16 = fneg <2 x double> %15
  %17 = tail call <2 x double> @llvm.fmuladd.v2f64(<2 x double> %16, <2 x double> %15, <2 x double> splat (double 3.000000e+00))
  %18 = extractelement <2 x double> %17, i64 0
  %19 = extractelement <2 x double> %17, i64 1
  %20 = fcmp olt double %18, %19
  %21 = select i1 %20, double %9, double %12
  %22 = select i1 %20, double %11, double %8
  %23 = fsub double %21, %22
  %24 = fcmp ogt double %23, %2
  br i1 %24, label %6, label %25, !llvm.loop !9

25:                                               ; preds = %6, %3
  %26 = phi double [ %1, %3 ], [ %21, %6 ]
  %27 = phi double [ %0, %3 ], [ %22, %6 ]
  %28 = fadd double %26, %27
  %29 = fmul double %28, 5.000000e-01
  ret double %29
}

; Function Attrs: nofree nounwind sspstrong uwtable
define dso_local range(i32 0, 2) i32 @main() local_unnamed_addr #1 {
  br label %1

1:                                                ; preds = %1, %0
  %2 = phi double [ %18, %1 ], [ 2.000000e+01, %0 ]
  %3 = phi double [ %17, %1 ], [ -1.000000e+01, %0 ]
  %4 = phi double [ %16, %1 ], [ 1.000000e+01, %0 ]
  %5 = fdiv double %2, 3.000000e+00
  %6 = fadd double %3, %5
  %7 = fsub double %4, %5
  %8 = insertelement <2 x double> poison, double %6, i64 0
  %9 = insertelement <2 x double> %8, double %7, i64 1
  %10 = fadd <2 x double> %9, splat (double -2.000000e+00)
  %11 = fneg <2 x double> %10
  %12 = tail call <2 x double> @llvm.fmuladd.v2f64(<2 x double> %11, <2 x double> %10, <2 x double> splat (double 3.000000e+00))
  %13 = extractelement <2 x double> %12, i64 0
  %14 = extractelement <2 x double> %12, i64 1
  %15 = fcmp olt double %13, %14
  %16 = select i1 %15, double %4, double %7
  %17 = select i1 %15, double %6, double %3
  %18 = fsub double %16, %17
  %19 = fcmp ogt double %18, 1.000000e-09
  br i1 %19, label %1, label %20, !llvm.loop !9

20:                                               ; preds = %1
  %21 = fadd double %16, %17
  %22 = fmul double %21, 5.000000e-01
  %23 = fadd double %22, -2.000000e+00
  %24 = tail call double @llvm.fabs.f64(double %23)
  %25 = fcmp ogt double %24, 0x3EB0C6F7A0B5ED8D
  br i1 %25, label %26, label %28

26:                                               ; preds = %20
  %27 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str, double noundef %22)
  br label %30

28:                                               ; preds = %20
  %29 = tail call i32 @puts(ptr nonnull dereferenceable(1) @str)
  br label %30

30:                                               ; preds = %28, %26
  %31 = phi i32 [ 1, %26 ], [ 0, %28 ]
  ret i32 %31
}

; Function Attrs: mustprogress nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none)
declare double @llvm.fabs.f64(double) #2

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr noundef readonly captures(none), ...) local_unnamed_addr #3

; Function Attrs: nofree nounwind
declare noundef i32 @puts(ptr noundef readonly captures(none)) local_unnamed_addr #4

; Function Attrs: nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none)
declare <2 x double> @llvm.fmuladd.v2f64(<2 x double>, <2 x double>, <2 x double>) #5

attributes #0 = { nofree norecurse nosync nounwind sspstrong memory(none) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { nofree nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #2 = { mustprogress nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none) }
attributes #3 = { nofree nounwind "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #4 = { nofree nounwind }
attributes #5 = { nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none) }

!llvm.module.flags = !{!0, !1, !2, !3}
!llvm.ident = !{!4}
!llvm.errno.tbaa = !{!5}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 8, !"PIC Level", i32 2}
!2 = !{i32 7, !"PIE Level", i32 2}
!3 = !{i32 7, !"uwtable", i32 2}
!4 = !{!"clang version 22.1.8"}
!5 = !{!6, !6, i64 0}
!6 = !{!"int", !7, i64 0}
!7 = !{!"omnipotent char", !8, i64 0}
!8 = !{!"Simple C/C++ TBAA"}
!9 = distinct !{!9, !10}
!10 = !{!"llvm.loop.mustprogress"}
