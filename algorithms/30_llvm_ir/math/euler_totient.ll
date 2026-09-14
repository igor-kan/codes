; ModuleID = 'algorithms/02_c/math/euler_totient.c'
source_filename = "algorithms/02_c/math/euler_totient.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@str = private unnamed_addr constant [66 x i8] c"[C EulerTotient] phi(1)=1 phi(12)=4 phi(100)=40 phi(7)=6 verified\00", align 1
@str.2 = private unnamed_addr constant [38 x i8] c"[C EulerTotient] FAILED: phi mismatch\00", align 1

; Function Attrs: nofree norecurse nosync nounwind sspstrong memory(none) uwtable
define dso_local i64 @euler_totient(i64 noundef %0) local_unnamed_addr #0 {
  %2 = icmp slt i64 %0, 4
  br i1 %2, label %3, label %7

3:                                                ; preds = %21, %1
  %4 = phi i64 [ %0, %1 ], [ %22, %21 ]
  %5 = phi i64 [ %0, %1 ], [ %23, %21 ]
  %6 = icmp sgt i64 %4, 1
  br i1 %6, label %27, label %30

7:                                                ; preds = %1, %21
  %8 = phi i64 [ %24, %21 ], [ 2, %1 ]
  %9 = phi i64 [ %23, %21 ], [ %0, %1 ]
  %10 = phi i64 [ %22, %21 ], [ %0, %1 ]
  %11 = srem i64 %10, %8
  %12 = icmp eq i64 %11, 0
  br i1 %12, label %13, label %21

13:                                               ; preds = %7, %13
  %14 = phi i64 [ %15, %13 ], [ %10, %7 ]
  %15 = sdiv i64 %14, %8
  %16 = srem i64 %15, %8
  %17 = icmp eq i64 %16, 0
  br i1 %17, label %13, label %18, !llvm.loop !9

18:                                               ; preds = %13
  %19 = sdiv i64 %9, %8
  %20 = sub nsw i64 %9, %19
  br label %21

21:                                               ; preds = %7, %18
  %22 = phi i64 [ %15, %18 ], [ %10, %7 ]
  %23 = phi i64 [ %20, %18 ], [ %9, %7 ]
  %24 = add nuw nsw i64 %8, 1
  %25 = mul nuw nsw i64 %24, %24
  %26 = icmp sgt i64 %25, %22
  br i1 %26, label %3, label %7, !llvm.loop !11

27:                                               ; preds = %3
  %28 = sdiv i64 %5, %4
  %29 = sub nsw i64 %5, %28
  br label %30

30:                                               ; preds = %27, %3
  %31 = phi i64 [ %29, %27 ], [ %5, %3 ]
  ret i64 %31
}

; Function Attrs: nofree nounwind sspstrong uwtable
define dso_local range(i32 0, 2) i32 @main() local_unnamed_addr #1 {
  br label %3

1:                                                ; preds = %17
  %2 = icmp sgt i64 %18, 1
  br i1 %2, label %23, label %26

3:                                                ; preds = %17, %0
  %4 = phi i64 [ %20, %17 ], [ 2, %0 ]
  %5 = phi i64 [ %19, %17 ], [ 12, %0 ]
  %6 = phi i64 [ %18, %17 ], [ 12, %0 ]
  %7 = srem i64 %6, %4
  %8 = icmp eq i64 %7, 0
  br i1 %8, label %9, label %17

9:                                                ; preds = %3, %9
  %10 = phi i64 [ %11, %9 ], [ %6, %3 ]
  %11 = sdiv i64 %10, %4
  %12 = srem i64 %11, %4
  %13 = icmp eq i64 %12, 0
  br i1 %13, label %9, label %14, !llvm.loop !9

14:                                               ; preds = %9
  %15 = sdiv i64 %5, %4
  %16 = sub nsw i64 %5, %15
  br label %17

17:                                               ; preds = %14, %3
  %18 = phi i64 [ %11, %14 ], [ %6, %3 ]
  %19 = phi i64 [ %16, %14 ], [ %5, %3 ]
  %20 = add nuw nsw i64 %4, 1
  %21 = mul nuw nsw i64 %20, %20
  %22 = icmp sgt i64 %21, %18
  br i1 %22, label %1, label %3, !llvm.loop !11

23:                                               ; preds = %1
  %24 = sdiv i64 %19, %18
  %25 = sub nsw i64 %19, %24
  br label %26

26:                                               ; preds = %1, %23
  %27 = phi i64 [ %25, %23 ], [ %19, %1 ]
  %28 = icmp eq i64 %27, 4
  br i1 %28, label %31, label %59

29:                                               ; preds = %45
  %30 = icmp sgt i64 %46, 1
  br i1 %30, label %51, label %54

31:                                               ; preds = %26, %45
  %32 = phi i64 [ %48, %45 ], [ 2, %26 ]
  %33 = phi i64 [ %47, %45 ], [ 100, %26 ]
  %34 = phi i64 [ %46, %45 ], [ 100, %26 ]
  %35 = srem i64 %34, %32
  %36 = icmp eq i64 %35, 0
  br i1 %36, label %37, label %45

37:                                               ; preds = %31, %37
  %38 = phi i64 [ %39, %37 ], [ %34, %31 ]
  %39 = sdiv i64 %38, %32
  %40 = srem i64 %39, %32
  %41 = icmp eq i64 %40, 0
  br i1 %41, label %37, label %42, !llvm.loop !9

42:                                               ; preds = %37
  %43 = sdiv i64 %33, %32
  %44 = sub nsw i64 %33, %43
  br label %45

45:                                               ; preds = %42, %31
  %46 = phi i64 [ %39, %42 ], [ %34, %31 ]
  %47 = phi i64 [ %44, %42 ], [ %33, %31 ]
  %48 = add nuw nsw i64 %32, 1
  %49 = mul nuw nsw i64 %48, %48
  %50 = icmp sgt i64 %49, %46
  br i1 %50, label %29, label %31, !llvm.loop !11

51:                                               ; preds = %29
  %52 = sdiv i64 %47, %46
  %53 = sub nsw i64 %47, %52
  br label %54

54:                                               ; preds = %29, %51
  %55 = phi i64 [ %53, %51 ], [ %47, %29 ]
  %56 = icmp ne i64 %55, 40
  %57 = select i1 %56, ptr @str.2, ptr @str
  %58 = zext i1 %56 to i32
  br label %59

59:                                               ; preds = %54, %26
  %60 = phi ptr [ @str.2, %26 ], [ %57, %54 ]
  %61 = phi i32 [ 1, %26 ], [ %58, %54 ]
  %62 = tail call i32 @puts(ptr nonnull dereferenceable(1) %60)
  ret i32 %61
}

; Function Attrs: nofree nounwind
declare noundef i32 @puts(ptr noundef readonly captures(none)) local_unnamed_addr #2

attributes #0 = { nofree norecurse nosync nounwind sspstrong memory(none) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { nofree nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #2 = { nofree nounwind }

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
!11 = distinct !{!11, !10}
