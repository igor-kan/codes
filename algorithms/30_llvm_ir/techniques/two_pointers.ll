; ModuleID = 'algorithms/02_c/techniques/two_pointers.c'
source_filename = "algorithms/02_c/techniques/two_pointers.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@__const.main.a = private unnamed_addr constant [5 x i32] [i32 1, i32 2, i32 3, i32 4, i32 6], align 16
@str = private unnamed_addr constant [42 x i8] c"[C TwoPointers] FAILED: existing pair 2+4\00", align 1
@str.3 = private unnamed_addr constant [49 x i8] c"[C TwoPointers] Two-sum on sorted array verified\00", align 1
@str.4 = private unnamed_addr constant [37 x i8] c"[C TwoPointers] FAILED: phantom pair\00", align 1

; Function Attrs: nofree norecurse nosync nounwind sspstrong memory(argmem: read) uwtable
define dso_local range(i32 0, 2) i32 @two_sum(ptr noundef readonly captures(none) %0, i32 noundef %1, i32 noundef %2) local_unnamed_addr #0 {
  %4 = icmp sgt i32 %1, 1
  br i1 %4, label %5, label %26

5:                                                ; preds = %3
  %6 = add nsw i32 %1, -1
  br label %7

7:                                                ; preds = %5, %18
  %8 = phi i32 [ %24, %18 ], [ %6, %5 ]
  %9 = phi i32 [ %21, %18 ], [ 0, %5 ]
  %10 = zext nneg i32 %9 to i64
  %11 = getelementptr inbounds nuw i32, ptr %0, i64 %10
  %12 = load i32, ptr %11, align 4, !tbaa !5
  %13 = sext i32 %8 to i64
  %14 = getelementptr inbounds i32, ptr %0, i64 %13
  %15 = load i32, ptr %14, align 4, !tbaa !5
  %16 = add nsw i32 %15, %12
  %17 = icmp eq i32 %16, %2
  br i1 %17, label %26, label %18

18:                                               ; preds = %7
  %19 = icmp slt i32 %16, %2
  %20 = zext i1 %19 to i32
  %21 = add nuw nsw i32 %9, %20
  %22 = xor i1 %19, true
  %23 = sext i1 %22 to i32
  %24 = add nsw i32 %8, %23
  %25 = icmp slt i32 %21, %24
  br i1 %25, label %7, label %26, !llvm.loop !9

26:                                               ; preds = %18, %7, %3
  %27 = phi i32 [ 0, %3 ], [ 1, %7 ], [ 0, %18 ]
  ret i32 %27
}

; Function Attrs: nofree nounwind sspstrong uwtable
define dso_local range(i32 0, 2) i32 @main() local_unnamed_addr #1 {
  br label %1

1:                                                ; preds = %12, %0
  %2 = phi i32 [ %18, %12 ], [ 4, %0 ]
  %3 = phi i32 [ %15, %12 ], [ 0, %0 ]
  %4 = zext nneg i32 %3 to i64
  %5 = getelementptr inbounds nuw i32, ptr @__const.main.a, i64 %4
  %6 = load i32, ptr %5, align 4, !tbaa !5
  %7 = sext i32 %2 to i64
  %8 = getelementptr inbounds i32, ptr @__const.main.a, i64 %7
  %9 = load i32, ptr %8, align 4, !tbaa !5
  %10 = add nsw i32 %9, %6
  %11 = icmp eq i32 %10, 6
  br i1 %11, label %20, label %12

12:                                               ; preds = %1
  %13 = icmp slt i32 %10, 6
  %14 = zext i1 %13 to i32
  %15 = add nuw nsw i32 %3, %14
  %16 = xor i1 %13, true
  %17 = sext i1 %16 to i32
  %18 = add nsw i32 %2, %17
  %19 = icmp slt i32 %15, %18
  br i1 %19, label %1, label %39, !llvm.loop !9

20:                                               ; preds = %1, %31
  %21 = phi i32 [ %37, %31 ], [ 4, %1 ]
  %22 = phi i32 [ %34, %31 ], [ 0, %1 ]
  %23 = zext nneg i32 %22 to i64
  %24 = getelementptr inbounds nuw i32, ptr @__const.main.a, i64 %23
  %25 = load i32, ptr %24, align 4, !tbaa !5
  %26 = sext i32 %21 to i64
  %27 = getelementptr inbounds i32, ptr @__const.main.a, i64 %26
  %28 = load i32, ptr %27, align 4, !tbaa !5
  %29 = add nsw i32 %28, %25
  %30 = icmp eq i32 %29, 12
  br i1 %30, label %39, label %31

31:                                               ; preds = %20
  %32 = icmp slt i32 %29, 12
  %33 = zext i1 %32 to i32
  %34 = add nuw nsw i32 %22, %33
  %35 = xor i1 %32, true
  %36 = sext i1 %35 to i32
  %37 = add nsw i32 %21, %36
  %38 = icmp slt i32 %34, %37
  br i1 %38, label %20, label %39, !llvm.loop !9

39:                                               ; preds = %12, %31, %20
  %40 = phi ptr [ @str.4, %20 ], [ @str.3, %31 ], [ @str, %12 ]
  %41 = phi i32 [ 1, %20 ], [ 0, %31 ], [ 1, %12 ]
  %42 = tail call i32 @puts(ptr nonnull dereferenceable(1) %40)
  ret i32 %41
}

; Function Attrs: nofree nounwind
declare noundef i32 @puts(ptr noundef readonly captures(none)) local_unnamed_addr #2

attributes #0 = { nofree norecurse nosync nounwind sspstrong memory(argmem: read) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
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
